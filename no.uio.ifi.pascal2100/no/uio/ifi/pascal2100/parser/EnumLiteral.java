package no.uio.ifi.pascal2100.parser;

import static no.uio.ifi.pascal2100.scanner.TokenKind.nameToken;

import no.uio.ifi.pascal2100.main.Main;
import no.uio.ifi.pascal2100.scanner.*;

public class EnumLiteral extends PascalDecl {

	public EnumType ent;
	public String name;
	public EnumLiteral nextEt;

	public EnumLiteral(String id, int lNum) {
		super(id, lNum);
		// TODO Auto-generated constructor stub
	}

	
	@Override public String identify() {
		return "<enum literal> " + name + " on line " + lineNum;
		}

	@Override
	void prettyPrint() {
		// TODO Auto-generated method stub
		Main.log.prettyPrint( name );
	}

	public static EnumLiteral parse(Scanner s) {
		// TODO Auto-generated method stub
		enterParser("enum literal");
		s.test(nameToken);
		EnumLiteral elt= new EnumLiteral(s.curToken.id,s.curLineNum());
		elt.name=s.curToken.id;
		s.readNextToken();
		leaveParser("enum literal");
		return elt;
	}


	@Override
	public void check(Block curScope, Library lib) {
		// TODO Auto-generated method stub
		curScope.decls.put(name, this);
		
	}

}
