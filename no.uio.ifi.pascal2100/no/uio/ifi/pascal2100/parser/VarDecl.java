package no.uio.ifi.pascal2100.parser;

import static no.uio.ifi.pascal2100.scanner.TokenKind.*;

import java.util.ArrayList;

import no.uio.ifi.pascal2100.main.Main;
import no.uio.ifi.pascal2100.scanner.Scanner;



/**
 * <h1>VarDecl</h1>
 *
 * <p>Parse a Pascal VarDecl as per project jernbarnediagram</p>
 *
 * <p>Copyright (c) 2015 by Sameer Sawant</p>
 */
public class VarDecl extends PascalDecl {

	public VarDeclPart vardecle;
	Type tp;
	public VarDecl nextvardec;
	 public ArrayList<VarDecl>  vardecl = new ArrayList<VarDecl>();;
	public  String name;
	
	public VarDecl(String id, int lNum) {
		super(id, lNum);
		// TODO Auto-generated constructor stub
	}
	
	/**
     * Parse a VarDecl.
     * @param Scanner Tokens.
     * @return the VarDeclobject of the parse tree.
     * name ---:---- type--- ;--
     */

	public static VarDecl parse(Scanner s) {
		
		enterParser("var decl");
		s.test(nameToken);
		VarDecl vd = new VarDecl(s.curToken.id,s.curLineNum());
		vd.name=s.curToken.id;
		vd.vardecl.add(vd);
		s.readNextToken();
		s.skip(colonToken);
		vd.tp=Type.parse(s);vd.tp.vadecl=vd;
		
		s.skip(semicolonToken);
		leaveParser("var decl ");
		return vd;
	}
	@Override
	public String identify() {
		// TODO Auto-generated method stub
		return "<var decl > "  +" on line " + lineNum;
	}

	@Override void prettyPrint() {
		
		Main.log.prettyPrint(name);
		Main.log.prettyPrint(":");
		tp.prettyPrint();
		Main.log.prettyPrint(";");
		}

	@Override
	public void check(Block curScope, Library lib) {
		// TODO Auto-generated method stub
		
		if (tp!= null) tp.check(curScope, lib);
}

		
}

	


